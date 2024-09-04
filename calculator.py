def main(): #added by contributor
    b=input('enter the expression') #added by contributor
    return b    #added by contributor

a = main()

original_lst=list()
original_lst_1=list()
original_lst_2=list()
original_lst_3=list()

for i in a :
    if a.index(i)!=len(a)-1:
        if i==a[a.index(i)+1]:
            original_lst.append(i+a[a.index(i)+1])
        else:
            original_lst.append(i)
    else:
        original_lst.append(i)


for i in original_lst:
    if i=='/':
        div_index=original_lst.index(i)
        div_index_copy=div_index
        numerator=float(original_lst[div_index-1])
        denominator=float (original_lst[div_index+1])
        if denominator == 0: #added by contributor
            print("Cannot Divide by zero")  #added by contributor
            main() #added by contributor
        div_result=numerator/denominator
        del original_lst[div_index-1:div_index+2]
        original_lst.insert(div_index_copy-1,div_result)


for i in original_lst:
    original_lst_1.append(str(i))

for i in original_lst_1:
    if i=='*':
        mul_index=original_lst_1.index(i) 
        term_one=float(original_lst_1[mul_index-1])
        term_two=float(original_lst_1[mul_index+1])
        mul_result=term_one*term_two
        del original_lst_1[mul_index-1:mul_index+2]
        original_lst_1.insert(mul_index-1,mul_result)


for i in original_lst_1:
    original_lst_2.append(str(i))


for i in original_lst_2:
    if i=='+':
        add_index=original_lst_2.index(i)
        term_one=float(original_lst_2[add_index-1])
        term_two=float(original_lst_2[add_index+1])
        add_result=term_one+term_two
        del original_lst_2[add_index-1:add_index+2]
        original_lst_2.insert(add_index-1,add_result)


for i in original_lst_2:
    original_lst_3.append(str(i))


for i in original_lst_3:
    if i=='-':
        sub_index=original_lst_3.index(i)
        term_one=float(original_lst_3[sub_index-1])
        term_two=float(original_lst_3[sub_index+1])
        sub_result=term_one-term_two
        del original_lst_3[sub_index-1:sub_index+2]
        original_lst_3.insert(sub_index-1,sub_result)
        
        


print('THE RESULT OF THE FOLLOWING EXPRESSION IS',original_lst_3[0])          

b=int(input(''))       
