(define (cddr s) (cdr (cdr s)))

(define (cadr s) 'YOUR-CODE-HERE
    (car (cdr s))
)

(define (caddr s) 'YOUR-CODE-HERE
    (car (cddr s))
)

(define (sign num) 'YOUR-CODE-HERE
    (cond
        ((> num 0) 1)
        ((< num 0) -1)
        (else 0)
    )
)

(define (square x) (* x x))

(define (pow x y) 'YOUR-CODE-HERE
    (if (= y 1) x
        (if (even? y)
            (square (pow x (/ y 2)))
            (* x (pow x (- y 1)))
        )
    )
)

(define (unique s) 'YOUR-CODE-HERE
    (if (null? s) nil
        (cons (car s) (unique (filter (lambda (x) (not (eq? x (car s)))) (cdr s))))
    )    
)

(define (replicate x n) 'YOUR-CODE-HERE
    (define (replicate_helper x n s)
        (if (= n 0) s
            (replicate_helper x (- n 1) (cons x s))
        )
    )
    (replicate_helper x n nil)
)

(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
  (define (helper combiner i term)
    (if (= i n) (term n)
        (combiner (term i) (helper combiner (+ i 1) term))
    )
  )
  (combiner start (helper combiner 1 term))
)

(define (accumulate-tail combiner start n term)
  'YOUR-CODE-HERE
  (define (helper combiner i term ans)
    (if (= i n) (combiner (term n) ans)
      (helper combiner (+ i 1) term (combiner ans (term i)))
    )
  )
  (helper combiner 1 term start)
)

(define-macro
 (list-of map-expr for var in lst if filter-expr)
 'YOUR-CODE-HERE
 `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst))
)

(list-of (* x x) for x in '(3 4 5) if (odd? x))