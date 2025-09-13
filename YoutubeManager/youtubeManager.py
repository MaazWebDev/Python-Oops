import sqlite3

con = sqlite3.connect('youtube_videos.db')
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS Videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL   
            
    )
''')

def list_videos():
    cur.execute('SELECT * FROM Videos')
    for row in cur.fetchall():
        print(row)

def add_video(name,time):
    cur.execute('INSERT INTO Videos (name , time) VALUES (?,?)', (name ,time))
    con.commit()


def update_video(video_id,new_name,new_time):
    cur.execute('UPDATE Videos SET name = ?, time = ? WHERE id = ?' , (new_name,new_time,video_id))
    con.commit()

def delete_video(video_id):
    cur.execute('DELETE FROM Videos WHERE id = ?',(video_id,))
    con.commit()


def main():
    while True:
        print('\n Youtube Manager App With DB')
        print('1. List Videos')
        print('2. Add Videos')
        print('3. Update Videos')
        print('4. Delete Videos')
        print('5. Exit App')
        choice = input('Enter Your Choice : ')

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input('Enter The Video Name : ')
            time = input('Enter The Video Time : ')
            add_video(name,time)
        elif choice == '3':
            video_id = input('Enter Video Id To Update : ')
            name = input('Enter The Video Name : ')
            time = input('Enter The Video Time : ')
            update_video(video_id,name,time)
        elif choice == '4':
            video_id = input('Enter Video Id To Delete : ')

            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print('Invalid Choice')
    
    con.close()


if __name__ == "__main__":
    main()