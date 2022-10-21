/**

Object-based box class that requires casting every time you want to get some specific stuff from it, e.g.:

    Box cakeBox = new Box();
    cakeBox.put(new Cake());
    // Without casting only object can be retrieved out of the box
    Cake cake = (Cake) cakeBox.get();

Casting is not desirable and can fall at runtime, could you create more... generic solution?

*/
class Box<Item> {

    private Item item;

    public void put(Item item) {
    	this.item = item;
    }

    public Item get() {
        return this.item;
    }

}