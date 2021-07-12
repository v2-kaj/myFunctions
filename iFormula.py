def cal(principle, bank_interest_rate, duration, loan_interest, profit, total_contributions):
	money_back=principle+(principle*(bank_interest_rate/100)*(duration/12))+((loan_interest+profit)*(principle/total_contributions))
	return money_back
	
print(cal(2500,2,12,89000,0,1117452.19)+cal(2000,2,11,89000,0,1117452.19)+ cal(1500,2,10,89000,0,1117452.19)) #for Ganizani


july = cal(2500,2,12,89000,0,1117452.19)
august =cal(2000,2,11,89000,0,1117452.19)
september =cal(2000,2,10,89000,0,1117452.19)
october =cal(5000,2,9,89000,0,1117452.19)
november =cal(4000,2,8,89000,0,1117452.19)
december =cal(4000,2,7,89000,0,1117452.19)

print(july+august+september+october+november+december) #for Florence
print(2500+2000+2000+5000+4000+4000)
	


