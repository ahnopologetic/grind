class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # brute force
        # set <- 0) separated by @ get split[0] 1) ignore . before @, 2) ignore after first +. If there are more than one +, think about this later.
        res = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.replace(".", "")
            if "+" in local:
                plus_index = local.find("+")
                local = local[:plus_index]
            res.add(local + '@' + domain)
        return len(res)
