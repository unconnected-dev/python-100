#Unique Email Addresses
#https://leetcode.com/problems/unique-email-addresses/description/

caseEmails_1 = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
caseEmails_2 = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]

if True:
    def numUniqueEmails(emails):
        res = set()

        for email in emails:
            if len(email) > 0:
                prefix = email.split("@")[0]
                affix = email.split("@")[1]
                
                if "+" in prefix:
                    res.add(prefix.split("+")[0].replace(".","") + "@" + affix)
                else:
                    res.add(prefix.replace(".","") + "@" + affix)
        
        return len(res)
    
print(f"{numUniqueEmails(caseEmails_1)}")
print(f"{numUniqueEmails(caseEmails_2)}")