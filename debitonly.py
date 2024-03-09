import dns_network_api as dnsnetwork
import dns_bank_api as dnsbank
import time




def delay(delaytime):
    time.sleep(delaytime)



# Forgive me, for what I have done in the name of speed

arr1 = ["Jacob", "Cole","vendor2"]
arr2 = ["8699541993827635120","12747177873692660996","12189830934118122652"]
def main():
  while(True):
    delay(5)
    # if dnsnetwork.network_check("102") != 0:
    #   # seperate the input from the network into respective lines
    #   test = (dnsnetwork.network_request(102)).split("\n")   

      # filter input 
    # print(dnsbank.bank_get_info("8699541993827635120"))
    if (dnsnetwork.network_check(102)):
        test = (dnsnetwork.network_request(102)).split("\n")   
        if (len(test) != 4):
            # This is importnatnt
            print("Noting in tube")
        else:
            test2 = (test[0][12:len(test[0])-1]).split(",") 
            code = test2[1]
            # Don't need to strip
            id = (test2[0]).strip("en")
            count = 0

            
            price = test[1][8:len(test[1])-1]
            vendor = (test[2][9:len(test[2])-1])

            for i in arr1:
                if i == vendor:
                    vendor = arr2[count]
                count = count + 1

            # print(code + " " + id + " " + price + " " + vendor)
            print(dnsnetwork.network_request("102"))
            #make code to parce pull from network pwetty pwease ^w^
            fromID = id
            amount = price
            vendorID = vendor
            fromCode = code
            #bank.bank_verify(fromID, "CODE", code)

            
            thing2 = dnsbank.bank_get_info(fromID).split("\n")
            print(thing2)
            thing3 = dnsbank.bank_get_info(vendorID).split("\n")
            print(thing3)
            # if int(thing2[1 ][4:]) > amount:
            print(fromID + "/"+vendorID + "/"+fromCode+ "/"+ amount)
            dnsbank.bank_transfer(fromID, vendorID, fromCode, amount)
    # print(dnsbank.bank_get_info("8699541993827635120"))   
    
main()

# while (True):

#     account_from = "12747177873692660996"
#     secure_code = "1480048740"
#     amount = "10"
#     account_to = "8699541993827635120"  
#     # print(dnsbank.bank_custom(f"transfer\n{account_from}\n{secure_code}\n{amount}\n{account_to}"))
#     # print(dnsnetwork.network_custom("102\nExtracted Payload: {\nCard Data: {Jakkfjdk\n))
   
#     print(dnsnetwork.network_check(102))
#     # print(dnsnetwork.network_request(102))

#     if (dnsnetwork.network_check(102)):
#         test = (dnsnetwork.network_request(102)).split("\n")   
#         if (len(test) != 4):
#             break
#         test2 = (test[0][12:len(test[0])-1]).split(",") 
#         code = test2[1]
#         id = (test2[0]).strip("en")
#         price = test[1][8:len(test[1])-1]
#         vendor = (test[2][9:len(test[2])-1])
#         print(code + " " + id + " " + price + " " + vendor)
        









    # print(dnsbank.bank_get_info("8699541993827635120"))

    # delay(5)
    # result = dnsnetwork.network_check("102")
    # test = dnsnetwork.network_request("102")
    # print(result)
    # if (test != "Data: NULL"):
    # print(test)

