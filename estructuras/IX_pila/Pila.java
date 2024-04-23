import java.util.Stack;

public class Pila<T> implements IPila<T> {
    private Stack<T> items;

    public Pila() {
        this.items = new Stack<>();
    }

    public boolean isEmpty() {
        return items.isEmpty();
    }

    public void stack(T item) {
        items.push(item);
    }
    
    public T unStack() {
        return items.pop();
    }
    
    public T peek() {
        return items.peek();
    }
}
    