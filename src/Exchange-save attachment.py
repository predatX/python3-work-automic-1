from exchangelib import Account, credentials, FileAttachment, Credentials

#域名\\邮箱姓名
credentials = Credentials(username='cop\\predat', password='passwd')

account = Account('predat@exchange.com', credentials=credentials, autodiscover=True)
print('1.Connected to B exchangw~~')

print(account.inbox.children)
for item in account.inbox.children:
    print('Running the FOR now~')
    print('2.文件夹名称:'+item.name)
    if item.name=='XRAY':#只要XRAY文件夹下的附件
        index=0
        totalcount=0
        page=0
        while True:
            for model in item.all()[page:page+50]:
                index=index+1
                print(str(index)+'-开始:'+model.subject)
                for attachment in model.attachments:
                    if isinstance(attachment, FileAttachment):
                        with open('D:\\Cache\\cache\\' + attachment.name, 'wb') as f:
                            f.write(attachment.content)
            if totalcount==index:
                break
            page=page+50
            totalcount=index