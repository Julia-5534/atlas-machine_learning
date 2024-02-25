-- Creates a function SafeDiv
DELIMITER //
DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
BEGIN
    DECLARE result FLOAT;
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;

    RETURN result
END;//
DELIMITER ;
