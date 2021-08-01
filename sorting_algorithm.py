def sorting_algorithm(li):
	new_li = list()
	p = 0 #pivot
	while len(li)>1:
                # finding the current min and max value 
		maxnum = max(li)
		max_index = li.index(maxnum)
		minnum = min(li)
		min_index = li.index(minnum)

                #moving it to new list
		#this conditioning is done to avoid shifting the index
		if min_index > max_index:
			li.remove(li[min_index])
			li.remove(li[max_index])
		elif min_index < max_index:
			li.remove(li[max_index])
			li.remove(li[min_index])

		new_li.insert(0+p,minnum)
		new_li.insert(1+p, maxnum)
		p += 1 # shifting the pivot

	if len(li) == 1: # in case the number of items in list is odd
		leftover = li[0]
		new_li.insert(0+p, leftover)

	return new_li # returns sorted list





