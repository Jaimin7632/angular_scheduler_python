import {Injectable} from '@angular/core';
import {DayPilot} from 'daypilot-pro-angular';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable()
export class DataService {

  constructor(private http: HttpClient) {
  }

  getEvents(from: DayPilot.Date, to: DayPilot.Date): Observable<any[]> {
    return this.http.get("/api/backend_events.php?from=" + from + "&to=" + to) as Observable<any>;
  }

  getResources(): Observable<any[]> {
    return this.http.get("/api/backend_resources.php") as Observable<any>;
  }

  createEvent(data: any): Observable<DataResponse> {
    return this.http.post("/api/backend_create.php", data) as Observable<DataResponse>;
  }

  moveEvent(data: any): Observable<DataResponse> {
    return this.http.post("/api/backend_move.php", data) as Observable<DataResponse>;
  }

}

export interface DataResponse {
  result: string;
  id?: number;
  message?: string;
}

