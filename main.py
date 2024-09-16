import sqlite3
from utils import bcolors

# minitodolist by arya

con = sqlite3.connect('minitodolist.db')
cur = con.cursor()

def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS todo (id INTEGER PRIMARY KEY, task TEXT, status TEXT)')
    con.commit()

def add_task(task):
    cur.execute('INSERT INTO todo (task, status) VALUES (?, ?)', (task, 'Not Done'))
    con.commit()

def show_tasks():
    cur.execute('SELECT * FROM todo')
    tasks = cur.fetchall()
    for task in tasks:
        print(task)
    if not tasks:
        print(f'{bcolors.WARNING}No tasks available{bcolors.ENDC}')

def task_exists(task_id):
    cur.execute('SELECT * FROM todo WHERE id = ?', (task_id,))
    task = cur.fetchone()
    if task:
        return True
    return False

def mark_as_done(task_id):
    cur.execute('UPDATE todo SET status = ? WHERE id = ?', ('Done', task_id))
    con.commit()

def delete_task(task_id):
    try:
        cur.execute('DELETE FROM todo WHERE id = ?', (task_id,))
        con.commit()
        print(f'{bcolors.OKGREEN}Task {task_id} deleted successfully{bcolors.ENDC}')
    except:
        print(f'{bcolors.FAIL}Task not found{bcolors.ENDC}')

def main():
    print(f'{bcolors.OKGREEN}Welcome to Mini Todo List{bcolors.ENDC}')
    print(f'{bcolors.OKCYAN}Tip: enter "0" at any time to see this list again...{bcolors.ENDC}\n')
    create_table()
    print('1. Add Task')
    print('2. Show Tasks')
    print('3. Mark as Done')
    print('4. Delete Task')
    print('5. Exit')

    while True:
        try:
            choice = int(input(f'\n{bcolors.OKBLUE}Enter your choice: {bcolors.ENDC}'))
        except:
            print(f'{bcolors.FAIL}Invalid choice{bcolors.ENDC}')
            continue
        if choice == 0:
            print('1. Add Task')
            print('2. Show Tasks')
            print('3. Mark as Done')
            print('4. Delete Task')
            print('5. Exit')
        if choice == 1:
            task = input('\n-> Creating new task... Enter task name or enter "0" to cancel: ')
            if task == '0':
                continue
            add_task(task)
            print(f'{bcolors.OKGREEN}Task "{task}" added successfully{bcolors.ENDC}')
        elif choice == 2:
            show_tasks()
        elif choice == 3:
            task_id = int(input('\n-> Marking as done... Enter task id or enter "0" to cancel: '))
            if task_id == 0:
                continue
            mark_as_done(task_id)
            print(f'{bcolors.OKGREEN}Task {task_id} marked as done{bcolors.ENDC}')
        elif choice == 4:
            task_id = int(input('\n-> Deleting task... Enter task id or enter "0" to cancel: '))
            if task_id == 0:
                continue
            if task_exists(task_id):
                delete_task(task_id)
            else:
                print(f'{bcolors.FAIL}Task {task_id} not found{bcolors.ENDC}')
        elif choice == 5:
            break
        else:
            print(f'{bcolors.FAIL}Invalid choice{bcolors.ENDC}')

if __name__ == '__main__':
    main()