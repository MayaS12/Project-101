from os import access, read
import dropbox

class TransferData:
        def __init__(self, access_token):
            self.access_token = access_token

        def uploadFile(self, fileFrom, fileTo):
            dbx = dropbox.Dropbox(self.access_token)
            f = open(fileFrom, 'rb')
            dbx.files_upload(f.read(), fileTo)

def main():
        access_token = "b22unrDPuzMAAAAAAAAAAS51JlOQiuco3apCI_YfND8epkA0qDRwZiRUFvdxnjdH"

        transferData = TransferData(access_token)

        fileFrom = input("Enter file path")
        fileTo = input("Enter the dropbox path")

        transferData.uploadFile(fileFrom, fileTo)

        print("File completed")

main()