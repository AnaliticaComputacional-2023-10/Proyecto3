SELECT *
FROM TRANSFORMED2
WHERE FAMI_ESTRATOVIVIENDA NOT IN ('Sin Estrato')
AND FAMI_EDUCACIONMADRE NOT IN ('No Aplica', 'No sabe')
AND FAMI_EDUCACIONPADRE NOT IN ('No Aplica', 'No sabe');