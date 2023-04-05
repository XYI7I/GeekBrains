BEGIN TRANSACTION
DECLARE @user_id INT = <id_пользователя>

DELETE FROM messages WHERE user_id = @user_id
DELETE FROM likes WHERE user_id = @user_id
DELETE FROM media WHERE user_id = @user_id
DELETE FROM communities WHERE user_id = @user_id
DELETE FROM users WHERE id = @user_id

COMMIT TRANSACTION

SELECT @user_id