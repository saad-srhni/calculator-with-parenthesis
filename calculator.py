class calculatrice:
    def __init__(self,chaine):
        l=list(chaine)
        i=0
        for u in l:
            if u =='(':
                i+=1
            elif u==')':
                i-=1
        if i!=0:
            print("erreur syntax")
        else :
            self.ch=chaine
        
    def conv(self):
        l=list(self.ch)
        self.listnumber=[]
        self.listopr=[]
        self.listdeg=[]
        j=0
        i=0
        k=0
        h=0
        for u in l:
            if u in ['0','1','2','3','4','5','6','7','8','9']:
                i=i*10+int(u)
                h=1
                if k == len(l)-1:
                    self.listnumber.append(i)
            elif u in ['*','/','-','+']:
                if h==1:
                    self.listnumber.append(i)
                    i=0
                    h=0
                self.listopr.append(u)
                if u in ['+','-']:
                    self.listdeg.append(j+1)
                else :
                    self.listdeg.append(j+2)
            elif u in ['(',')']:
                if i!=0 and h==1:
                    self.listnumber.append(i)
                    i=0
                    h=0
                if u =='(':
                    j+=3
                else :
                    j-=3
            else :
                print("stop run !!")
                break
            k+=1
        

    def calculer(self):
        def operation(n,o,m):
            if o =='+':
                return n+m
            elif o=='-':
                return n-m
            elif o=='*':
                return n*m
            elif o=='/':
                try :
                    return float(n)/m
                exception :
                    print("erreur can not /0")
                
        d=self.listdeg
        n=self.listnumber
        o=self.listopr
        i=0
        while(len(n)!=1):
            p= d.index(max(d))
            res=operation(n[p],o[p],n[p+1])
            n.pop(p)
            n.pop(p)
            o.pop(p)
            d.pop(p)
            n.insert(p,res)
        return n[0]
            
            
                
  
