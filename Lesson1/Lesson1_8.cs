bool IsEvenNumber(int num) => num % 2 == 0;

IReadOnlyList<int> EvenNumbers(int N)
{
    var evenNums = new List<int>();
    for (int i = 2; i <= N; i += 2)
        evenNums.Add(i);

    return evenNums;
}

Console.Write("Введите число N: ");
var N = int.Parse(Console.ReadLine());


Console.WriteLine($"{N} -> {string.Join(", ", EvenNumbers(N))}");