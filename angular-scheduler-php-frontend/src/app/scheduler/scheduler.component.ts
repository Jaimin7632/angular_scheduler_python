import {Component, ViewChild, AfterViewInit} from '@angular/core';
import {DayPilot, DayPilotSchedulerComponent} from 'daypilot-pro-angular';
import {DataService} from './data.service'; {}

@Component({
  selector: 'scheduler-component',
  template: `<daypilot-scheduler [config]="config" [events]="events" #scheduler></daypilot-scheduler>`,
  styles: [``]
})
export class SchedulerComponent implements AfterViewInit {

  @ViewChild('scheduler', {static: false})
  scheduler: DayPilotSchedulerComponent;

  events: any[] = [];

  config: any = {
    scale: "Day",
    startDate: DayPilot.Date.today().firstDayOfMonth(),
    days: DayPilot.Date.today().daysInMonth(),
    timeHeaders: [
      {groupBy: "Month"},
      {groupBy: "Day", format: "d"}
    ],
    cellWidthSpec: "Auto",
    resources: [],
    treeEnabled: true,
    onBeforeEventRender: args => {
      if (args.data.text && args.data.text === "Vacation") {
        args.data.barColor = "#0F9D58";
        args.data.barBackColor = "#0F9D58";
      }
    },
    onEventMove: args => {
      let data = {
        id: args.e.id(),
        newStart: args.newStart.toString(),
        newEnd: args.newEnd.toString(),
        newResource: args.newResource
      };

      this.ds.moveEvent(data).subscribe(result => {
        this.scheduler.control.message("Updated");
      });
    },
    onEventResize: args => {
      let data = {
        id: args.e.id(),
        newStart: args.newStart.toString(),
        newEnd: args.newEnd.toString(),
        newResource: args.e.resource()  // existing resource id
      };

      this.ds.moveEvent(data).subscribe(result => {
        this.scheduler.control.message("Updated");
      });
    },
    onTimeRangeSelect: args => {

      DayPilot.Modal.prompt("Event name: ", "New event").then(modal => {
        if (modal.canceled) {
          return;
        }
        this.scheduler.control.clearSelection();
        var e = {
          id: null,
          start: args.start.toString(),
          end: args.end.toString(),
          text: modal.result,
          resource: args.resource
        };

        this.ds.createEvent(e).subscribe(result => {
          e.id = result.id;
          this.events.push(e);
          this.scheduler.control.message("Created");
        });
      });
    }
  };

  constructor(private ds: DataService) {
  }

  ngAfterViewInit(): void {
    this.ds.getResources().subscribe(result => this.config.resources = result);

    const from = this.scheduler.control.visibleStart();
    const to = this.scheduler.control.visibleEnd();
    this.ds.getEvents(from, to).subscribe(result => {
      this.events = result;
    });
  }

}

