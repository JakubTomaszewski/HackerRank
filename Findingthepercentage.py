if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

def get_avr(name):
    return '{:0.2f}'.format(sum(student_marks[name])/3)

print(get_avr(query_name))
