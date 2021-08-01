
def generate_moves_list(n):
    def make_moves(n, origin, auxiliar, target):
        # save.append((origin.copy(),  target.copy(), auxiliar.copy(), 'bottom2'))
        if n == 1:
            target.append(origin.pop())
            save.append((rod_1.copy(), rod_2.copy(), rod_3.copy()))

        if n > 1:
            make_moves(n-1, origin, target, auxiliar)
            target.append(origin.pop())
            save.append((rod_1.copy(), rod_2.copy(), rod_3.copy()))
            make_moves(n-1, auxiliar, origin, target)

    rod_1, rod_2, rod_3 = [i for i in range(n, 0, -1)], [], []
    save = [(rod_1.copy(), rod_2.copy(), rod_3.copy())]
    make_moves(n, rod_1, rod_2, rod_3)
    return save
