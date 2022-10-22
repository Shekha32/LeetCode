#Implement Stack using Queues
class MyStack:

        def __init__(self):
                self.stack = []

        def push ( self, x: int ) -> None:
                self.stack.append ( x )
        
        def pop ( self ) -> int:
                return self.stack.pop()

        def top ( self ) -> int:
                return self.stack [ -1 ]

        def empty ( self ) -> bool:
                return True if len ( self.stack ) == 0 else False
        

def main ():
        # Your MyStack object will be instantiated and called as such:
        obj = MyStack()
        obj.push ( 1 )
        obj.push ( 3 )
        obj.push ( 5 )
        param_2 = obj.pop()
        param_3 = obj.top()
        param_4 = obj.empty()

        assert param_2 == 5
        assert param_3 == 3
        assert param_4 == False

main ()
