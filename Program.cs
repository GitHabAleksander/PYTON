// Задача 10: Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа.
// 456 -> 5
// 782 -> 8
// 918 -> 1

Console.WriteLine("Введи трехзначное число:");
string? number = Console.ReadLine();
int numberA = Convert.ToInt32(number);
if ((numberA / 100 > 0) && (numberA / 1000 == 0))
{
    Console.WriteLine("Число трехзначное");
    int midNumber = (numberA % 100) / 10;
    Console.WriteLine(midNumber);
}
else
{
    Console.WriteLine("Введено не трехзначное число");
}
