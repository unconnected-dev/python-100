#Subdomain Visit Count
#https://leetcode.com/problems/subdomain-visit-count/description/

caseCpdomains_1 = ["9001 discuss.leetcode.com"]
caseCpdomains_2 = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

if False:
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

if True:
    def subdomainVisits(cpdomains):
        my_hash = {}
        
        for cp in cpdomains:
            count, domain = cp.split()
            count = int(count)
            subdomains = domain.split(".")
            
            for i in range(len(subdomains)):
                subdomain = ".".join(subdomains[i:])
                my_hash[subdomain] = my_hash.get(subdomain, 0) + count
                
        return [f"{count} {domain}" for domain, count in my_hash.items()]                    
        
print(f"{subdomainVisits(caseCpdomains_1)}")
print(f"{subdomainVisits(caseCpdomains_2)}")