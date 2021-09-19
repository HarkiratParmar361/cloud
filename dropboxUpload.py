# where code start line #:2,3, 28,29,16,17,18,19,20,5,6,20,21,22,23,24,25,26,8,9,10,11,12,13,14,15,27,29-end of program
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'm4PUEQt7SyYAAAAAAAAAAY1m3QBtCim8qlT8DI3K6ihJjh1Bu0n_yUT5KOgKGA72'
    
    #creating object transfer data for class TransferData. whenever you create an object for a class it will automatically call the constructor of the class. 
    transferDataObject = TransferData(access_token)

    file_from = '/Applications/Harkirat white hat jr/Python/class101/test.txt'
    file_to = '/testwhitehatdropbox/test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferDataObject.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()
