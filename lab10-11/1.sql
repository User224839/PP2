CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(username TEXT, surname TEXT, phone TEXT) AS
$$
BEGIN
    RETURN QUERY
    SELECT username, surname, phone
    FROM phonebook
    WHERE username ILIKE '%' || pattern || '%'
       OR surname ILIKE '%' || pattern || '%'
       OR phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;
