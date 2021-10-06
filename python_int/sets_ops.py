skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}

# print(skills.intersection(job_skills))    # method

venny = skills & job_skills                 # operator
print(" ".join(venny))                      # formatted answer

# operators
print(skills & job_skills)                  # intersection
print(skills | job_skills)                  # union
print(skills - job_skills)                  # difference
print(job_skills - skills)                  # difference
print(skills ^ job_skills)                  # symmetric difference
