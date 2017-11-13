
## Eksempel på hvordan en kan bruke ODESolver til å løse radioactive_decay
import ODESolver

# Her skal en Decay - klasse være definert.
# Se s.790 for eksempel på hvordan klassen skal defineres.
# I eksempelet på s.790 er kun metodene __init__ og __call__ viktige radioactive_decay-oppgaven

if __name__ == '__main__':
    a = # Fra oppgaven
    problem = Decay(a) # Her sendes inn 'problemet' som skal løses
    solver = ODESolver.<numerisk metode>(problem) # Her velges hvilken numerisk metode skal brukes.
                                                  # Erstatt <numerisk metode> med en metode som du vil bruke
    solver.set_initial_condition(problem.u0) # Sett startbetingelse
    dt = # Fra oppgaven
    n = # Fra oppgaven
    T = # Fra oppgaven
    t = # Lag n+1 verdier fra 0 til T
    u,t = solver.solve(t) # Finn løsning
