// See https://aka.ms/new-console-template for more information
Console.WriteLine("Задача с двумя друзьями и собакой.");
int count = 0;
int distance = 10000;
int first_friend_speed = 1;
int second_friend_speed = 2;
int dog_speed = 5;
int friend = 2;
int time = 0;
while (distance > 10)
{
    if (friend == 1)
    {
        time = distance / (first_friend_speed + dog_speed);
        friend = 2;
    }
        
    else
    {
        time = distance / (second_friend_speed + dog_speed);
        friend = 1;
    }
        
    distance = distance - (first_friend_speed + second_friend_speed) * time;
    count++;
}
    
Console.WriteLine("Собака встретит друзей " + count + " раз");