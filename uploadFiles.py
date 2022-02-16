import dropbox

class TransferData:
    def __init__(self,accessToken):
        self.accessToken=accessToken
    def upload_file(self,fileFrom,fileTo):
        dpx=dropbox.Dropbox(self.accessToken) 
        f=open(fileFrom,"rb")
        dpx.files_upload(f.read(),fileTo)  
        
def main():
    accessToken="hTsRyVuk87gAAAAAAAAAASNoyDnRHO3IQId4izk4uROBxRzKNLV0TbtDzwjw_Eg9"
    transferData=TransferData(accessToken)
    fileFrom="E:\Win10\Desktop\dpx"
    fileTo="/Dpx1/"    
    transferData.upload_file(fileFrom, fileTo)
    print("File has been moved!")
main()