CREATE TRIGGER tr_check_community_name
ON communities
AFTER INSERT
AS
BEGIN
    IF (SELECT LEN(name) FROM inserted) < 5
    BEGIN
        RAISERROR ('Название сообщества должно быть не менее 5 символов', 16, 1)
        ROLLBACK TRANSACTION
    END
END