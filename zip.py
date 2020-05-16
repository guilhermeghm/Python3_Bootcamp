midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']

#final_grades = [max(pair) for pair in zip(midterms, finals)]
#final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}
#print(final_grades)

'''
#To calculate the max grade.
final_grades = dict(
    zip(
        students,
        map(
            lambda pair: max(pair),
            zip(midterms, finals)

        )
    )
)

print(final_grades)
'''

#To calculate the avg grade.
avg_grades = dict(
    zip(
        students,
        map(
            lambda pair: ((pair[0]+pair[1])/2),
            zip(midterms, finals)

        )
    )
)

print(avg_grades)
