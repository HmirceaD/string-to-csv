import csv

words = "shipping,shipped,ship,9.95,rip off,ripoff,fraud,scam,scammers,china,aliexpress,www.aliexpress.com,ebay,ebay.com,www.ebay.com,4.95,6.95,$,7.95,$,20,sucks,fuck,thieves,thief,expensive,high,price,http,https,://,www,shipping,ship,ships,shipped,shipping fees,how much to ship,9.95,$9.95,$50,50 bucks,no way,rippoff,ripoff,fraud,scam,scammers,beware,make these,make this,ebay,aliexpress,china,s & handling,s&handling,s& handling,9.95,995,16,37,47,received it,gotten it,received theirs,received theres,gotten theres,recieved one,received one,10,$10,10.00,$10!,$10.00!,not free,where is it,where is my order,when will it come,how long will it take,how long,shipping,deliver,delivered,amazon,amazon.com,19.90,$19.90,50,$50,$20,20,$30,30,$40,40,$29.85,29.85,$39.80,39.80,$49.75,49.75,two weeks,2 weeks,3 weeks,three weeks,4 weeks,four weeks,month,waiting,month ago,forever ago,still haven't gotten,still not here,still have not received,received,recieved,catch,charge,credit,credit card,creditcard,paypal,pay pal,month,s&h,cheap,skeptical,sceptical,review,reviews,30$,20$,10$,$,40$,50$,60$,70$,deliver,delivered,amazon,amazon.com,19.90,$19.90,50,$50,$20,20,$30,30,$40,40,$29.85,29.85,$39.80,39.80,$49.75,49.75,two weeks,2 weeks,3 weeks,three weeks,4 weeks,four weeks,month,waiting,month ago,forever ago,still haven't gotten,still not here,still have not received,legit,paypal,paypal,sketchy,make mine,make my own,make one,has anyone ordered,hidden,hidden fee,hidden fees,leery,leary,scared,dont trust,don't trust,bs,bullshit,do not order,don't order,dont order,months ago,weeks ago,paypal,took the money,took my money,took money,never sent,never shipped"

word_list = words.split(",")

print(type(word_list))

with open('words.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(word_list)

