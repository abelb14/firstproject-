import json
import os


def main():
    FILE_PATH = './data.json'

    if os.path.isfile(FILE_PATH):
        print('Press 1 to add a new book \n Press 2 to delete a book \n Press 3 to find author of book')
        option = input('Please enter an option: ')

        if option is 1 or option is '1':
            # Add a new book
            add_book(FILE_PATH)
        elif option is 2 or option is '2':
            # Delete a book
            delete_book(FILE_PATH)
        elif option is 3 or option is '3':
            find_author(FILE_PATH)
        else:
            print('Unkown option')
    else:
        print('File not found')

# Define functions here


def add_book(file_path):
    book_title = input('Please enter a book title: ').lower().strip()
    author = input('Please enter an author name: ').lower().strip()
    handle_add_or_delete(file_path, False, book_title, author)
# Delete book function


def delete_book(file_path):
    book_title = input('Please enter book title to delete: ').lower().strip()
    handle_add_or_delete(file_path, True, book_title)


def find_author(file_path):
    book_title = input('Please enter a book title: ').lower().strip()
    with open(file_path, 'r') as data_file:
        data = json.load(data_file)
        if book_title in data:
            print("Author of {} is {}".format(
                book_title, data[book_title]))
        else:
            print('Unable to find book')


def handle_add_or_delete(file_path, is_delete, book_title, author=None):
    data_file = open(file_path, 'r')
    data = json.load(data_file)
    data_file.close()

    if is_delete:
        if book_title in data:
            del data[book_title]
        else:
            print('Not book found with {}'.format(book_title))
    else:
        if book_title not in data:
            data[book_title] = author
        else:
            print('Book {} already exists'.format(book_title))

    data_file = open(file_path, 'w')
    data_file.write(json.dumps(data))
    data_file.close()


# Run main function
main()
