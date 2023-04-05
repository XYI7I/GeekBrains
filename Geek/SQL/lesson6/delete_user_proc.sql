CREATE PROCEDURE sp_delete_user
    @user_id INT
AS
BEGIN
    BEGIN TRANSACTION

    DELETE FROM messages WHERE user_id = @user_id
    DELETE FROM likes WHERE user_id = @user_id
    DELETE FROM media WHERE user_id = @user_id
    DELETE FROM communities WHERE user_id = @user_id
    DELETE FROM users WHERE id = @user_id

    COMMIT TRANSACTION

    SELECT @user_id
END