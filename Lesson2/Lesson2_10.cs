int ParseSecondDigitNumber(int num) => (num / 10) % 10;

Console.Write("Введите 3-ех значное число: ");
var num = int.Parse(Console.ReadLine());

Console.WriteLine($"{num} -> {ParseSecondDigitNumber(num)}");