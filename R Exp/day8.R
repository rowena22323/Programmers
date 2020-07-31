smsraw<-read.csv("sms_spam_ansi.txt",
         stringsAsFactors = FALSE)
str(smsraw)
smsraw$type<-factor(smsraw$type)
str(smsraw)
table(smsraw$type)
