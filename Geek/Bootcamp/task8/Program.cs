// See https://aka.ms/new-console-template for more information
const int N = 1000; // size matrix
const int THREADS_NUMBER = 8;
                    
int[,] serialMulRes = new int[N, N];
int[,] threadMulRes = new int[N, N];

int[,] firstMatrix = MatrixGenerator(N, N);
int[,] secondMatrix = MatrixGenerator(N, N);

SerialMatrixMul(firstMatrix, secondMatrix);
PrepareParalleMatrixMul(firstMatrix, secondMatrix);
Console.WriteLine(EqualityMatrix(serialMulRes, threadMulRes));


int[,] MatrixGenerator(int rows, int columns)
{
    Random _rand = new Random();
    int[,] res = new int[rows, columns];
    for (int i = 0; i < res.GetLength(0); i++)
    {
        for (int j = 0; j < res.GetLength(1); j++)
        {
            res[i, j] = _rand.Next(-100, 100);
        }
    }
    return res;
}

void SerialMatrixMul(int[,] a, int[,] b)
{
    if (a.GetLength(1) != b.GetLength(0)) throw new Exception("Can't multiplay such matrix!");
    for (int i = 0; i < a.GetLength(0); i++)
    {
        for(int j = 0; j < b.GetLength(1); j++)
        {
            for(int k = 0; k < b.GetLength(0); k++)
            {
                serialMulRes[i, j] = a[i, k] * b[k, j];
            }
                
        }
    }
}

void PrepareParalleMatrixMul(int[,] a, int[,] b)
{
    if (a.GetLength(1) != b.GetLength(0)) throw new Exception("Can't multiplay such matrix!");
    int eachThreadCalc = N / THREADS_NUMBER;
    var threadList = new List<Thread>();
    for (int i = 0; i < THREADS_NUMBER; i++)
    {
        int startPos = i * eachThreadCalc;
        int endPos = (i + 1) * eachThreadCalc;
        // final thread
        if (i == THREADS_NUMBER - 1) endPos = N;
        threadList.Add(new Thread(() => ParallelMatrixMul(a, b, startPos, endPos)));
        threadList[i].Start();
    }
    for (int i = 0; i < THREADS_NUMBER; i++)
    {
        threadList[i].Join();
    }    
}

void ParallelMatrixMul(int[,] a, int[,] b, int startPos, int endPos)
{
    for (int i = startPos; i < endPos; i++)
    {
        for(int j = 0; j < b.GetLength(1); j++)
        {
            for(int k = 0; k < b.GetLength(0); k++)
            {
                threadMulRes[i, j] = a[i, k] * b[k, j];
            }
                
        }
    }
}

bool EqualityMatrix(int[,] fmatrix, int[,] smatrix)
{
    bool res = true;

    for (int i = 0; i < fmatrix.GetLength(0); i++)
    {
        for (int j = 0; j < fmatrix.GetLength(1); j++)
        {
            res = res && (fmatrix[i, j] == smatrix[i, j]);
        }
    }

    return res;
}
