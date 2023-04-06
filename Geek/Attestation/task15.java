public class Counter implements AutoCloseable {
    private int count = 0;
    private boolean isClosed = false;

    public void add() {
        if (isClosed) {
            throw new IllegalStateException("Counter is closed");
        }
        count++;
    }

    @Override
    public void close() {
        isClosed = true;
        System.out.println("Counter is closed");
    }

    public int getCount() {
        return count;
    }
}

// Чтобы использовать объект этого класса в блоке try-with-resources, можно написать следующий код:

try (Counter counter = new Counter()) {
    // код для заведения нового животного и увеличения счетчика
} catch (Exception e) {
    // обработка исключения
}