def cal(principle, bank_interest_rate, duration, loan_interest, profit, total_contributions):
	money_back=principle+(principle*(bank_interest_rate/100)*(duration/12))+((loan_interest+profit)*(principle/total_contributions))
	return money_back

#print(cal(2500,2,12,89000,0,1117452.19)+cal(2000,2,11,89000,0,1117452.19)+ cal(1500,2,10,89000,0,1117452.19)) #for Ganizani
#july = cal(2500,2,12,89000,0,1117452.19)
#august =cal(2000,2,11,89000,0,1117452.19)
#september =cal(2000,2,10,89000,0,1117452.19)
#october =cal(5000,2,9,89000,0,1117452.19)
#november =cal(4000,2,8,89000,0,1117452.19)
#december =cal(4000,2,7,89000,0,1117452.19)
#print(july+august+september+october+november+december) #for Florence

#print(2500+2000+2000+5000+4000+4000)

#For TK
#print(Tjuly)
#Taugust =cal(2000,2,11,109000,0,1210961.75)
#print(Taugust)
'''Tjuly = (cal(2500,2,12,109000,0,1210961.75))
Tseptember =cal(2500,2,10,109000,0,1210961.75)
print(Tseptember)
Toctober =cal(4000,2,9,109000,0,1210961.75)
print(Toctober)
Tnovember =cal(4000,2,8,109000,0,1210961.75)
print(Tnovember)
Tdecember =cal(5000,2,7,109000,0,1210961.75)
print(Tdecember)
Tjanuary =cal(3000,2,6,109000,0,1210961.75)
print(Tjanuary)'''

#print(2500+2000+2500+4000+4000+5000+3000)

#print(Tjuly+Taugust+Tseptember+Toctober+Tnovember+Tdecember+Tjanuary)
'''totalContribution = 994522.75
Cjuly = cal(2500,2,14,198000,0,totalContribution)

Caugust =cal(2000,2,13,198000,0,totalContribution)

Cseptember =cal(2500,2,12,198000,0,totalContribution)

Coctober =cal(4000,2,11,198000,0,totalContribution)

Cnovember =cal(4000,2,10,198000,0,totalContribution)

Cdecember =cal(5000,2,9,198000,0,totalContribution)

Cjanuary =cal(16500,2,8,198000,0,totalContribution)

Cfebruary =cal(16500,2,7,198000,0,totalContribution)

Cmarch =cal(17500,2,6,198000,0,totalContribution)

Capril =cal(16500,2,5,198000,0,totalContribution)

Cmay =cal(3000,2,4,198000,0,totalContribution)

Cjune=cal(32000,2,3,198000,0,totalContribution)

Cjuly2 =cal(0,2,2,198000,0,totalContribution)

Caugust2 =cal(0,2,1,198000,0,totalContribution)

CtotalContributions = 2500+2000+2500+4000+4000+5000+16500+16500+17500+16500+3000+32000
money = Cjuly+Caugust+Cseptember+Coctober+Cnovember+Cdecember+Cjanuary+Cfebruary+Cmarch+Capril+ Cmay + Cjune + Cjuly2 + Caugust2

Cloan = 0
expenses = 43990.44
Cexpenses = expenses/10
CmoneyBack = money-Cloan-Cexpenses
print("Total Contributions ", CtotalContributions)
print("Total Loans ", Cloan)
print("Total Expenses Share ", Cexpenses)
print("Total money back ", CmoneyBack)'''

totalContribution = 994522.75
pjuly = cal(2500,2,15,198000,0,totalContribution)

paugust =cal(2000,2,14,198000,0,totalContribution)

pseptember =cal(2500,2,13,198000,0,totalContribution)

poctober =cal(4000,2,12,198000,0,totalContribution)

pnovember =cal(4000,2,11,198000,0,totalContribution)

pdecember =cal(5000,2,10,198000,0,totalContribution)

pjanuary =cal(4000,2,9,198000,0,totalContribution)

pfebruary =cal(29000,2,8,198000,0,totalContribution)

pmarch =cal(17500,2,7,198000,0,totalContribution)

papril =cal(4000,2,6,198000,0,totalContribution)

pmay =cal(0,2,5,198000,0,totalContribution)

pjune=cal(0,2,4,198000,0,totalContribution)

pjuly2 =cal(0,2,3,198000,0,totalContribution)

paugust2 =cal(20000,2,2,198000,0,totalContribution)

ptotalContributions = 2500+2000+2500+4000+4000+5000+4000+29000+17500+4000+20000
money = pjuly+paugust+pseptember+poctober+pnovember+pdecember+pjanuary+pfebruary+pmarch+papril+ pmay + pjune + pjuly2 + paugust2

ploan = 0
expenses = 43990.44
pexpenses = expenses/10
pmoneyBack = money-ploan-pexpenses
print("Total Contributions ", ptotalContributions)
print("Total Loans ", ploan)
print("Total Expenses Share ", pexpenses)
print("Total money back ", pmoneyBack)
