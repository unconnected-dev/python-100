#Subdomain Visit Count
#https://leetcode.com/problems/subdomain-visit-count/description/

caseCpdomains_1 = ["9001 discuss.leetcode.com"]
caseCpdomains_2 = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

if True:
    def subdomainVisits(cpdomains):
        my_hash = {}
        
        for cp in cpdomains:
            count, long_domain = cp.split(" ")
            count = int(count)
            domains = long_domain.split(".")
            
            domain = ""
            for i in range(len(domains)-1,-1,-1):
                domain = domains[i] + domain    
                my_hash[domain] = my_hash.get(domain, 0) + count 
                domain = "." + domain
            
        res = []
        for key, val in my_hash.items():
            res.append(f"{val} {key}")
            
        return res
                
print(f"{subdomainVisits(caseCpdomains_1)}")
print(f"{subdomainVisits(caseCpdomains_2)}")