def namelist(names):
    result = ''
    
    for name in names:
        
        if name == names[len(names)-1]:
            result +=name['name']
        elif name == names[len(names)-2]:
            result +=name['name'] + ' & '
        else:
            result += name['name'] + ', '
        
        
    return result
print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]))
print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))
print(namelist([ {'name': 'Bart'} ]))
print(namelist([]))