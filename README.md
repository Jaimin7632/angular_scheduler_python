### Angular scheduler python implementation <br>
https://code.daypilot.org/67423/angular-scheduler-tutorial-typescript
<br><br>
### **Steps to run:**
1. Setup flask and peewee for python(>=3.5)
2. Install requirements.txt
3. Run
`python ./angular-scheduler-python-backend/app.py`
<br><br>
### **Code conversation:**

__db.php : /angular-scheduler-python-backend/database_utils/utils.py -> db_init()<br>
backend_create.php : /angular-scheduler-python-backend/database_utils/utils.py -> create_events()<br>
backend_resources.php : /angular-scheduler-python-backend/database_utils/utils.py -> get_backend_resources()<br>
backend_events.php : /angular-scheduler-python-backend/database_utils/utils.py -> get_backend_events()<br>
backend_move.php : /angular-scheduler-python-backend/database_utils/utils.py -> update_backend_move()<br>_
<br><br>
### **How code structure works ?**
1. Create api name with .php in app.py<br>`
@app.route('/api/backend_create.php', methods=['POST'])`<br>
   Note: _Reason of using .php in api is we don't want to change frontend for python changes. This will directly setup with current frontend._
   
2. Api call the database utils functions.