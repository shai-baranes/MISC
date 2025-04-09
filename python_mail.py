import win32com.client as win32 # you need to have a working outlook application
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'shai.baranes@gmail.com'
# mail.To = 'shai.baranes@philips.com'
mail.CC = 'shai.baranes@gmail.com'
# mail.CC = 'shai.baranes@philips.com'
mail.Subject = 'Test from Python'
# mail.Subject = 'Message subject'
mail.Body = 'if you get this email - bla bla bla\nBla'
# mail.HTMLBody = '<h1>HTML Message body\nBla Bla Bla</h1>' #this field is optional
# mail.HTMLBody = '<h2>HTML Message body</h2>' #this field is optional

# To attach a file to the email (optional):

# attachment  = "Path to the attachment"
# mail.Attachments.Add(attachment)

mail.Send()





# ".".join('Aaron.Magal'.split(' '))