try:
    #print(n)
    #a=int('codegnan')
    b=10+'20'
    l=[1,2,3,4]
    #print(l[10])
    k={1:1,2:2,3:3}
    #print(k[4])
    #a=10/0
except Exception as e:
    print("Error occured:",e)
else:
    print("No Error Occured")
finally:
    print("End the block")
'''except NameError:
    print("name 'n' is not defined")
except ValueError:
    print("Enter the valid datatype")
except TypeError:
    print("Give the proper datatype")
except IndexError:
    print("Index not found")
except KeyError:
    print("Key is not present")
except ZeroDivisionError:
    print("can't divide with zero")
'''
'''except(NameError,ValueError,TypeError,IndexError,KeyError,ZeroDivisionError) as e:
    print("Error Occured:",e)'''
