def runge_rule(f, a, b, nodeNumber, method, mult):
    return (mult*abs(method(f, a, b, 2*nodeNumber)-method(f, a, b, nodeNumber)))
