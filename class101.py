import dropbox
class TransferData:
    def __init__(self,access_token): 
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.BHq5cVrNY62HgWIOiOFcRFiLaKMuZp_-sC6e8dsRCRLqjrufv5CfLSohV2tNz8rGqV9OPXlk0MCGXxwNucqN4Q1Jy8B39kKZIfaR4tPWXgEfaSv54cmIvM__D1XoJ6_4f9z4B7M'
    transferData=TransferData(access_token)
    file_from='test.txt'
    file_to='/test_dropbox/test.txt'
    transferData.upload_file(file_from,file_to)
    print("file has been moved")
if __name__=='__main__':

    main()
