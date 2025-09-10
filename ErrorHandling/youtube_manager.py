import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)
def list_all_videos(videos):
    print('\n')
    print('*' * 70)
    for index,video in enumerate(videos, start=1):
        print(f"{index}, {video['name']}, 'Duration : {video['time']}")
    print('\n')
    print('*' * 70)


def add_video(videos):
    name = input('Enter Your Video Name : ')
    time = input('Enter Your Video Time : ')
    videos.append({'name': name , 'time':time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input('Enter The Video Number To Update'))
    if 1 <= index <= len(videos):
        name = input('Enter The New Video Name')
        time = input('Enter The New Video Time')
        videos[index-1] = {'name':name , 'time':time}
        save_data_helper(videos)
    else:
        print('Invalid Index Selected')

def delete_video(videos):
    pass


def main():
    videos = load_data()
    while True:
        print('\n Youtube Manager | Choose An Option')
        print(' 1. List All Youtube Video')
        print(' 2. Add A Youtube Video')
        print(' 3. Update A Youtube Video')
        print(' 4. Delete A Youtube Video')
        print(' 5. Exit The App')
        choice = input('Enter Your Choice : ')
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print('Invalid Choice')

if __name__ == "__main__":
    main()