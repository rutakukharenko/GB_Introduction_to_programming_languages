bool IsEvenNumber(int num) => num % 2 == 0;

Console.Write("Введите число: ");
var num = int.Parse(Console.ReadLine());
var result = IsEvenNumber(num) ? "да" : "нет";

Console.WriteLine($"{num} -> {result}");