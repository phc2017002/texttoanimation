from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService

class CircularLinkedListExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))
        
        # Execute all sections in sequence
        self.introduction()
        self.linked_list_basics()
        self.circular_concept()
        self.node_structure()
        self.insertion_operations()
        self.deletion_operations()
        self.traversal_operations()
        self.advantages_disadvantages()
        self.real_world_applications()
        self.complexity_analysis()
        self.comparison_with_linear()
        self.conclusion()

    def introduction(self):
        """Introduction to circular linked lists"""
        with self.voiceover(text="Welcome to this comprehensive explanation of Circular Linked Lists, one of the fundamental data structures in computer science. Today, we'll explore what makes circular linked lists unique, how they work internally, and why they're essential for many real-world applications.") as tracker:
            title = Text("Circular Linked Lists", font_size=36, color=BLUE, weight=BOLD)
            title.to_edge(UP, buff=1.0)
            subtitle = Text("A Complete Guide", font_size=28, color=WHITE)
            subtitle.next_to(title, DOWN, buff=0.4)
            
            self.play(Write(title))
            self.play(FadeIn(subtitle))
            
        with self.voiceover(text="Unlike traditional linear linked lists that have a clear beginning and end, circular linked lists form a continuous loop. This circular structure enables efficient cyclic operations and has fascinating applications in operating systems, network protocols, and multimedia players.") as tracker:
            # Create a simple circular visualization
            circle_radius = 2.0
            nodes = VGroup()
            for i in range(6):
                angle = i * 60 * DEGREES
                node = Circle(radius=0.4, color=GREEN, fill_opacity=0.3)
                node.move_to(circle_radius * np.array([np.cos(angle), np.sin(angle), 0]))
                nodes.add(node)
            
            nodes.move_to(DOWN * 0.5)
            
            arrows = VGroup()
            for i in range(6):
                start_node = nodes[i]
                end_node = nodes[(i + 1) % 6]
                arrow = CurvedArrow(
                    start_node.get_center() + RIGHT * 0.3,
                    end_node.get_center() + LEFT * 0.3,
                    color=YELLOW,
                    angle=-TAU/6
                )
                arrows.add(arrow)
            
            self.play(Create(nodes))
            self.play(Create(arrows), run_time=2)
            
        # Cleanup
        self.play(FadeOut(*self.mobjects))

    def linked_list_basics(self):
        """Review basic linked list concepts"""
        with self.voiceover(text="Before diving into circular linked lists, let's briefly review the fundamentals of linked lists. A linked list is a linear data structure where elements, called nodes, are connected through pointers or references.") as tracker:
            title = Text("Linked List Fundamentals", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
        with self.voiceover(text="Each node in a linked list contains two main components: the data field, which stores the actual value, and the next pointer, which points to the next node in the sequence. In a traditional singly linked list, the last node's next pointer is set to null, indicating the end of the list.") as tracker:
            # Show a simple linear linked list
            node1 = self.create_node("5", LEFT * 4 + DOWN * 0.5)
            node2 = self.create_node("12", LEFT * 1.5 + DOWN * 0.5)
            node3 = self.create_node("8", RIGHT * 1.5 + DOWN * 0.5)
            node4 = self.create_node("NULL", RIGHT * 4.5 + DOWN * 0.5, is_null=True)
            
            arrow1 = Arrow(node1.get_right() + RIGHT * 0.1, node2.get_left() + LEFT * 0.1, 
                          color=YELLOW, buff=0.1, stroke_width=4)
            arrow2 = Arrow(node2.get_right() + RIGHT * 0.1, node3.get_left() + LEFT * 0.1, 
                          color=YELLOW, buff=0.1, stroke_width=4)
            arrow3 = Arrow(node3.get_right() + RIGHT * 0.1, node4.get_left() + LEFT * 0.1, 
                          color=RED, buff=0.1, stroke_width=4)
            
            head_label = Text("HEAD", font_size=20, color=GREEN)
            head_label.next_to(node1, UP, buff=0.3)
            
            self.play(Create(node1), Create(node2), Create(node3), Create(node4))
            self.play(Create(arrow1), Create(arrow2), Create(arrow3))
            self.play(Write(head_label))
            
        # Cleanup
        self.play(FadeOut(*self.mobjects))

    def circular_concept(self):
        """Explain the circular concept"""
        with self.voiceover(text="Now, here's where circular linked lists become interesting. Instead of having the last node point to null, in a circular linked list, the last node points back to the first node, creating a complete circle or loop.") as tracker:
            title = Text("The Circular Concept", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
        with self.voiceover(text="This circular connection fundamentally changes how we interact with the data structure. There's no true beginning or end—you can start traversing from any node and eventually return to your starting point. This makes circular linked lists perfect for applications that require continuous cycling through data.") as tracker:
            # Create circular linked list
            node1 = self.create_node("10", LEFT * 3 + DOWN * 0.8)
            node2 = self.create_node("20", UP * 1.5)
            node3 = self.create_node("30", RIGHT * 3 + DOWN * 0.8)
            
            # Arrows forming a circle
            arrow1 = CurvedArrow(
                node1.get_top() + UP * 0.1,
                node2.get_left() + LEFT * 0.1,
                color=YELLOW,
                angle=-TAU/6
            )
            arrow2 = CurvedArrow(
                node2.get_right() + RIGHT * 0.1,
                node3.get_top() + UP * 0.1,
                color=YELLOW,
                angle=-TAU/6
            )
            arrow3 = CurvedArrow(
                node3.get_bottom() + DOWN * 0.1,
                node1.get_bottom() + DOWN * 0.1,
                color=GREEN,
                angle=-TAU/4
            )
            
            circular_label = Text("Forms a Circle!", font_size=24, color=GREEN)
            circular_label.move_to(DOWN * 2.5)
            
            self.play(Create(node1), Create(node2), Create(node3))
            self.play(Create(arrow1), Create(arrow2))
            self.play(Create(arrow3), Write(circular_label))
            
        with self.voiceover(text="Notice the green arrow at the bottom. This is the key difference: the last node's next pointer doesn't point to null—it points back to the first node, completing the circle. This creates an infinite loop structure that we can traverse indefinitely.") as tracker:
            # Highlight the circular connection
            highlight = SurroundingRectangle(arrow3, color=RED, buff=0.1)
            self.play(Create(highlight))
            self.play(FadeOut(highlight))
            
        # Cleanup
        self.play(FadeOut(*self.mobjects))

    def node_structure(self):
        """Detailed explanation of node structure"""
        with self.voiceover(text="Let's examine the internal structure of a node in a circular linked list at the code level. Understanding this structure is crucial for implementing the data structure correctly.") as tracker:
            title = Text("Node Structure", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
        with self.voiceover(text="In most programming languages, we define a node using a class or structure. The node contains two essential fields: data, which holds the actual information we want to store—this could be an integer, string, or any other data type—and next, which is a pointer or reference to the next node in the circular chain.") as tracker:
            # Show code structure
            code = Code(
                code="""class Node {
    int data;
    Node* next;
    
    Node(int value) {
        data = value;
        next = NULL;
    }
}""",
                language="cpp",
                font_size=20,
                background="window",
                insert_line_no=False
            )
            code.scale(0.85)
            code.move_to(LEFT * 2.5 + DOWN * 0.3)
            
            self.play(Create(code))
            
        with self.voiceover(text="On the right, we can visualize how this structure looks in memory. The data field stores our value, and the next pointer holds the memory address of the next node. In a circular linked list, even the last node's next pointer contains a valid address—the address of the head node.") as tracker:
            # Visual representation
            box = Rectangle(height=1.8, width=1.5, color=WHITE)
            box.move_to(RIGHT * 3 + DOWN * 0.5)
            
            data_text = Text("data", font_size=18)
            data_text.move_to(box.get_top() + DOWN * 0.4)
            data_value = Text("42", font_size=22, color=YELLOW)
            data_value.next_to(data_text, DOWN, buff=0.15)
            
            divider = Line(box.get_left() + DOWN * 0.3, box.get_right() + DOWN * 0.3, color=GRAY)
            
            next_text = Text("next", font_size=18)
            next_text.move_to(box.get_bottom() + UP * 0.4)
            next_arrow = Arrow(ORIGIN, RIGHT * 0.5, color=GREEN, stroke_width=3)
            next_arrow.next_to(next_text, DOWN, buff=0.1)
            
            self.play(Create(box), Write(data_text), Write(data_value))
            self.play(Create(divider))
            self.play(Write(next_text), Create(next_arrow))
            
        # Cleanup
        self.play(FadeOut(*self.mobjects))

    def insertion_operations(self):
        """Demonstrate insertion operations"""
        with self.voiceover(text="Insertion is one of the fundamental operations we can perform on a circular linked list. There are three main insertion scenarios: inserting at the beginning, inserting at the end, and inserting at a specific position.") as tracker:
            title = Text("Insertion Operations", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
        with self.voiceover(text="Let's start with inserting at the beginning. First, we create a new node with our desired value. Then, we need to find the last node in the circular list—this is the node whose next pointer currently points to the head. We update this last node's next pointer to point to our new node, and set our new node's next pointer to point to the old head.") as tracker:
            # Initial circular list
            node1 = self.create_node("10", LEFT * 2.5 + DOWN * 0.5)
            node2 = self.create_node("20", ORIGIN + DOWN * 0.5)
            node3 = self.create_node("30", RIGHT * 2.5 + DOWN * 0.5)
            
            arrow1 = Arrow(node1.get_right() + RIGHT * 0.05, node2.get_left() + LEFT * 0.05, 
                          color=YELLOW, buff=0.05, stroke_width=3)
            arrow2 = Arrow(node2.get_right() + RIGHT * 0.05, node3.get_left() + LEFT * 0.05, 
                          color=YELLOW, buff=0.05, stroke_width=3)
            
            arc_arrow = CurvedArrow(
                node3.get_top() + UP * 0.1 + RIGHT * 0.2,
                node1.get_top() + UP * 0.1 + LEFT * 0.2,
                color=YELLOW,
                angle=-TAU/5
            )
            
            head_label = Text("HEAD", font_size=20, color=GREEN)
            head_label.next_to(node1, UP, buff=0.5)
            
            self.play(Create(node1), Create(node2), Create(node3))
            self.play(Create(arrow1), Create(arrow2), Create(arc_arrow))
            self.play(Write(head_label))
            
        with self.voiceover(text="Now we insert the value five at the beginning. Watch carefully as we create the new node above the current list, then update the pointers to maintain the circular structure. The old circular connection is broken and reformed to include our new node.") as tracker:
            # New node to insert
            new_node = self.create_node("5", LEFT * 2.5 + UP * 1.2)
            new_node_label = Text("New Node", font_size=18, color=RED)
            new_node_label.next_to(new_node, UP, buff=0.2)
            
            self.play(Create(new_node), Write(new_node_label))
            
            # Show the reconnection
            self.play(FadeOut(arc_arrow))
            
            new_arc = CurvedArrow(
                node3.get_top() + UP * 0.1 + RIGHT * 0.2,
                new_node.get_right() + RIGHT * 0.1,
                color=GREEN,
                angle=-TAU/6
            )
            new_to_old_head = Arrow(
                new_node.get_bottom() + DOWN * 0.05,
                node1.get_top() + UP * 0.05,
                color=GREEN,
                stroke_width=3
            )
            
            self.play(Create(new_arc), Create(new_to_old_head))
            
            # Update head label
            self.play(head_label.animate.next_to(new_node, LEFT, buff=0.3))
            
        # Cleanup
        self.play(FadeOut(*self.mobjects))

    def deletion_operations(self):
        """Demonstrate deletion operations"""
        with self.voiceover(text="Deletion operations in circular linked lists require special attention to maintain the circular structure. Just like insertion, we have three main deletion scenarios: deleting from the beginning, deleting from the end, and deleting a specific node.") as tracker:
            title = Text("Deletion Operations", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
        with self.voiceover(text="Let's demonstrate deleting the first node. We start with a circular linked list containing four nodes. To delete the head node, we must find the last node—the one whose next pointer points to the current head. Then we update the last node's next pointer to skip over the head and point to the second node instead.") as tracker:
            # Create initial list
            node1 = self.create_node("15", LEFT * 4 + DOWN * 0.5)
            node2 = self.create_node("25", LEFT * 1.5 + DOWN * 0.5)
            node3 = self.create_node("35", RIGHT * 1.5 + DOWN * 0.5)
            node4 = self.create_node("45", RIGHT * 4 + DOWN * 0.5)
            
            arrow1 = Arrow(node1.get_right() + RIGHT * 0.05, node2.get_left() + LEFT * 0.05,
                          color=YELLOW, buff=0.05, stroke_width=3)
            arrow2 = Arrow(node2.get_right() + RIGHT * 0.05, node3.get_left() + LEFT * 0.05,
                          color=YELLOW, buff=0.05, stroke_width=3)
            arrow3 = Arrow(node3.get_right() + RIGHT * 0.05, node4.get_left() + LEFT * 0.05,
                          color=YELLOW, buff=0.05, stroke_width=3)
            
            arc_arrow = CurvedArrow(
                node4.get_top() + UP * 0.1,
                node1.get_top() + UP * 0.1,
                color=YELLOW,
                angle=-TAU/5
            )
            
            head_label = Text("HEAD", font_size=20, color=GREEN)
            head_label.next_to(node1, UP, buff=0.5)
            delete_label = Text("Delete", font_size=20, color=RED)
            delete_label.next_to(node1, DOWN, buff=0.3)
            
            self.play(Create(node1), Create(node2), Create(node3), Create(node4))
            self.play(Create(arrow1), Create(arrow2), Create(arrow3), Create(arc_arrow))
            self.play(Write(head_label), Write(delete_label))
            
        with self.voiceover(text="Now watch as we remove node fifteen. The last node's pointer changes from pointing to node fifteen to pointing directly to node twenty-five, which becomes our new head. The old head node is isolated and can be freed from memory.") as tracker:
            # Highlight the node to delete
            highlight = SurroundingRectangle(node1, color=RED, buff=0.1)
            self.play(Create(highlight))
            
            # Show new connection
            new_arc = CurvedArrow(
                node4.get_top() + UP * 0.1,
                node2.get_top() + UP * 0.1,
                color=GREEN,
                angle=-TAU/4.5
            )
            
            self.play(
                FadeOut(arc_arrow),
                FadeOut(arrow1),
                Create(new_arc)
            )
            
            self.play(
                FadeOut(node1),
                FadeOut(highlight),
                FadeOut(delete_label),
                head_label.animate.next_to(node2, UP, buff=0.5)
            )
            
        # Cleanup
        self.play(FadeOut(*self.mobjects))

    def traversal_operations(self):
        """Demonstrate traversal"""
        with self.voiceover(text="Traversal in a circular linked list is unique because there's no natural stopping point like a null pointer. We need to be careful to avoid infinite loops. The standard approach is to keep track of where we started and stop when we return to that starting point.") as tracker:
            title = Text("Traversal Operations", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
        with self.voiceover(text="Let's visualize a complete traversal. We'll start at the head node and visit each node exactly once, moving clockwise around the circle. A common algorithm uses a do-while loop: we process the current node, move to the next node, and continue until we return to our starting position.") as tracker:
            # Create circular list
            positions = [
                LEFT * 3 + DOWN * 1,
                UP * 1.5,
                RIGHT * 3 + DOWN * 1,
                DOWN * 2
            ]
            values = ["A", "B", "C", "D"]
            nodes = VGroup()
            
            for i, (pos, val) in enumerate(zip(positions, values)):
                node = self.create_node(val, pos)
                nodes.add(node)
            
            self.play(Create(nodes))
            
            # Create arrows
            arrows = VGroup()
            for i in range(4):
                start = nodes[i]
                end = nodes[(i + 1) % 4]
                arrow = CurvedArrow(
                    start.get_center() + (end.get_center() - start.get_center()) * 0.15,
                    end.get_center() + (start.get_center() - end.get_center()) * 0.15,
                    color=YELLOW,
                    angle=-TAU/8
                )
                arrows.add(arrow)
            
            self.play(Create(arrows))
            
        with self.voiceover(text="Now let's trace through the traversal step by step. We start at node A, which is our head. We visit A, then move to B, then to C, then to D, and finally back to A. At this point, we've completed one full cycle and we stop. Each node is visited exactly once during this traversal.") as tracker:
            # Animate traversal
            current_label = Text("Current", font_size=20, color=GREEN)
            
            for i in range(5):  # Go around once and return to start
                node_index = i % 4
                current_label.next_to(nodes[node_index], RIGHT, buff=0.4)
                
                highlight = Circle(radius=0.55, color=GREEN, stroke_width=4)
                highlight.move_to(nodes[node_index].get_center())
                
                if i == 0:
                    self.play(Write(current_label), Create(highlight))
                else:
                    self.play(
                        current_label.animate.next_to(nodes[node_index], RIGHT, buff=0.4),
                        Transform(highlight, Circle(radius=0.55, color=GREEN, stroke_width=4).move_to(nodes[node_index].get_center()))
                    )
                self.wait(0.5)
            
            stop_text = Text("Stop! Back at start", font_size=22, color=RED)
            stop_text.move_to(DOWN * 2.5)
            self.play(Write(stop_text))
            
        # Cleanup
        self.play(FadeOut(*self.mobjects))

    def advantages_disadvantages(self):
        """Discuss pros and cons"""
        with self.voiceover(text="Like any data structure, circular linked lists have specific advantages and disadvantages that make them suitable for certain applications but not others. Understanding these trade-offs is essential for choosing the right data structure for your needs.") as tracker:
            title = Text("Advantages & Disadvantages", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
        with self.voiceover(text="On the advantages side, circular linked lists excel at cyclic operations. Any node can be reached from any other node by traversing forward, which is perfect for round-robin scheduling. They're also more memory efficient than doubly linked lists while still providing flexible insertion and deletion anywhere in the list. Additionally, implementing certain algorithms like Josephus problem becomes much more elegant with circular structures.") as tracker:
            # Advantages column
            adv_title = Text("Advantages", font_size=26, color=GREEN, weight=BOLD)
            adv_title.move_to(LEFT * 3.5 + UP * 2.3)
            
            advantages = VGroup(
                Text("• Efficient cyclic operations", font_size=20),
                Text("• Any node reachable from any other", font_size=20),
                Text("• No null pointer checks needed", font_size=20),
                Text("• Memory efficient", font_size=20),
                Text("• Perfect for round-robin tasks", font_size=20)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            advantages.next_to(adv_title, DOWN, buff=0.4)
            advantages.shift(RIGHT * 0.3)
            
            self.play(Write(adv_title))
            for adv in advantages:
                self.play(Write(adv), run_time=0.6)
                
        with self.voiceover(text="However, circular linked lists also have disadvantages. The lack of a clear endpoint makes traversal algorithms more complex—you must explicitly track when you've completed a full cycle. This increases the risk of creating infinite loops if not implemented carefully. Finding the last node requires traversing the entire list, which is O of n time complexity, and the circular structure can make debugging more challenging.") as tracker:
            # Disadvantages column
            disadv_title = Text("Disadvantages", font_size=26, color=RED, weight=BOLD)
            disadv_title.move_to(RIGHT * 3.5 + UP * 2.3)
            
            disadvantages = VGroup(
                Text("• Complex traversal logic", font_size=20),
                Text("• Risk of infinite loops", font_size=20),
                Text("• Finding last node is O(n)", font_size=20),
                Text("• More difficult to debug", font_size=20),
                Text("• Requires careful implementation", font_size=20)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            disadvantages.next_to(disadv_title, DOWN, buff=0.4)
            disadvantages.shift(RIGHT * 0.3)
            
            self.play(Write(disadv_title))
            for disadv in disadvantages:
                self.play(Write(disadv), run_time=0.6)
                
        # Cleanup
        self.play(FadeOut(*self.mobjects))

    def real_world_applications(self):
        """Show real-world applications"""
        with self.voiceover(text="Circular linked lists aren't just theoretical constructs—they have numerous practical applications in real-world software systems. Let's explore some of the most common and important use cases.") as tracker:
            title = Text("Real-World Applications", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
        with self.voiceover(text="One of the most famous applications is in operating system process scheduling. CPU schedulers use circular linked lists to implement round-robin scheduling, where each process gets a fixed time slice and then moves to the back of the queue. The circular structure makes this rotation seamless and efficient.") as tracker:
            # Application 1: Round-robin scheduling
            app1_title = Text("Round-Robin CPU Scheduling", font_size=24, color=YELLOW)
            app1_title.move_to(UP * 2.2)
            self.play(Write(app1_title))
            
            # Show process queue
            processes = VGroup()
            process_names = ["P1", "P2", "P3", "P4"]
            
            for i, name in enumerate(process_names):
                angle = i * TAU / 4
                pos = 1.5 * np.array([np.cos(angle), np.sin(angle), 0]) + DOWN * 0.3
                proc = self.create_node(name, pos)
                processes.add(proc)
            
            self.play(Create(processes))
            
            cpu_label = Text("CPU", font_size=20, color=RED)
            cpu_label.move_to(DOWN * 0.3)
            self.play(Write(cpu_label))
            
            # Animate rotation
            for i in range(4):
                highlight = SurroundingRectangle(processes[i], color=GREEN, buff=0.08)
                self.play(Create(highlight))
                self.play(FadeOut(highlight))
                
        self.play(FadeOut(*self.mobjects))
            
        with self.voiceover(text="Another important application is in multiplayer games and board games. When implementing turn-based systems, a circular linked list naturally represents the player order. After the last player's turn, it automatically wraps around to the first player, making the game loop continuous and intuitive.") as tracker:
            title = Text("Real-World Applications", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            app2_title = Text("Multiplayer Game Turns", font_size=24, color=YELLOW)
            app2_title.move_to(UP * 2.2)
            self.play(Write(app2_title))
            
            players = VGroup()
            player_names = ["Player 1", "Player 2", "Player 3", "Player 4"]
            colors = [RED, BLUE, GREEN, PURPLE]
            
            for i, (name, color) in enumerate(zip(player_names, colors)):
                angle = i * TAU / 4 + TAU / 8
                pos = 2.2 * np.array([np.cos(angle), np.sin(angle), 0]) + DOWN * 0.5
                
                player_box = Rectangle(height=0.6, width=1.8, color=color, fill_opacity=0.2)
                player_box.move_to(pos)
                player_text = Text(name, font_size=16)
                player_text.move_to(pos)
                
                player = VGroup(player_box, player_text)
                players.add(player)
            
            self.play(Create(players))
            
            turn_label = Text("Current Turn", font_size=18, color=YELLOW)
            
            for i in range(5):
                turn_label.next_to(players[i % 4], UP, buff=0.2)
                if i == 0:
                    self.play(Write(turn_label))
                else:
                    self.play(turn_label.animate.next_to(players[i % 4], UP, buff=0.2))
                self.wait(0.4)
                
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Media players also use circular linked lists for playlist management. When you enable repeat mode, the playlist loops continuously. The circular structure eliminates the need for special logic to jump from the last song back to the first—it happens automatically through the circular connection.") as tracker:
            title = Text("Real-World Applications", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            app3_title = Text("Music Playlist - Repeat Mode", font_size=24, color=YELLOW)
            app3_title.move_to(UP * 2.2)
            self.play(Write(app3_title))
            
            songs = VGroup(
                Text("♫ Song 1", font_size=20),
                Text("♫ Song 2", font_size=20),
                Text("♫ Song 3", font_size=20),
                Text("♫ Song 4", font_size=20)
            )
            
            for i, song in enumerate(songs):
                angle = i * TAU / 4
                pos = 2.0 * np.array([np.cos(angle), np.sin(angle), 0]) + DOWN * 0.5
                song.move_to(pos)
            
            self.play(Write(songs))
            
            playing = Text("▶ Now Playing", font_size=18, color=GREEN)
            
            for i in range(6):
                playing.next_to(songs[i % 4], DOWN, buff=0.25)
                if i == 0:
                    self.play(Write(playing))
                else:
                    self.play(playing.animate.next_to(songs[i % 4], DOWN, buff=0.25))
                self.wait(0.5)
                
        # Cleanup
        self.play(FadeOut(*self.mobjects))

    def complexity_analysis(self):
        """Analyze time and space complexity"""
        with self.voiceover(text="Understanding the time and space complexity of circular linked list operations is crucial for making informed decisions about when to use this data structure. Let's analyze the computational costs of various operations.") as tracker:
            title = Text("Complexity Analysis", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
        with self.voiceover(text="For insertion operations, inserting at the beginning when we maintain a tail pointer is O of one constant time, because we can directly access both the tail and head. However, if we only maintain a head pointer, we need to traverse the entire list to find the tail, making it O of n. Insertion at the end with a tail pointer is also O of one, but O of n without it.") as tracker:
            # Create table for complexities
            table_title = Text("Time Complexity", font_size=26, color=YELLOW)
            table_title.move_to(UP * 2.2)
            self.play(Write(table_title))
            
            operations = VGroup(
                Text("Operation", font_size=20, weight=BOLD),
                Text("Insert at Beginning", font_size=18),
                Text("Insert at End", font_size=18),
                Text("Delete at Beginning", font_size=18),
                Text("Delete at End", font_size=18),
                Text("Search", font_size=18),
                Text("Traversal", font_size=18)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            operations.move_to(LEFT * 3.8 + DOWN * 0.3)
            
            with_tail = VGroup(
                Text("With Tail", font_size=20, weight=BOLD, color=GREEN),
                MathTex(r"O(1)", font_size=24, color=GREEN),
                MathTex(r"O(1)", font_size=24, color=GREEN),
                MathTex(r"O(1)", font_size=24, color=GREEN),
                MathTex(r"O(n)", font_size=24, color=YELLOW),
                MathTex(r"O(n)", font_size=24, color=YELLOW),
                MathTex(r"O(n)", font_size=24, color=YELLOW)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            with_tail.move_to(LEFT * 0.8 + DOWN * 0.3)
            
            without_tail = VGroup(
                Text("Without Tail", font_size=20, weight=BOLD, color=RED),
                MathTex(r"O(n)", font_size=24, color=YELLOW),
                MathTex(r"O(n)", font_size=24, color=YELLOW),
                MathTex(r"O(n)", font_size=24, color=YELLOW),
                MathTex(r"O(n)", font_size=24, color=YELLOW),
                MathTex(r"O(n)", font_size=24, color=YELLOW),
                MathTex(r"O(n)", font_size=24, color=YELLOW)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            without_tail.move_to(RIGHT * 2.2 + DOWN * 0.3)
            
            self.play(Write(operations))
            self.play(Write(with_tail))
            self.play(Write(without_tail))
            
        with self.voiceover(text="Search and traversal operations always require O of n time in the worst case, as we may need to visit every node in the list. For space complexity, a circular linked list uses O of n space, where n is the number of nodes, since each node requires memory for its data and next pointer. This is the same as a linear linked list but more efficient than a doubly circular linked list which needs previous pointers as well.") as tracker:
            space_text = Text("Space Complexity: O(n)", font_size=24, color=BLUE)
            space_text.move_to(DOWN * 2.8)
            self.play(Write(space_text))
            
        # Cleanup
        self.play(FadeOut(*self.mobjects))

    def comparison_with_linear(self):
        """Compare with linear linked list"""
        with self.voiceover(text="To fully appreciate circular linked lists, let's compare them side-by-side with their linear counterparts. This comparison will highlight the key differences and help you understand when to choose one over the other.") as tracker:
            title = Text("Circular vs Linear Linked Lists", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
        with self.voiceover(text="The most obvious difference is the structure. In a linear linked list, the last node's next pointer is null, creating a definite end point. In a circular linked list, the last node points back to the first, creating a continuous loop with no true beginning or end. This structural difference has profound implications for how we use these data structures.") as tracker:
            # Linear list on left
            linear_label = Text("Linear", font_size=24, color=YELLOW)
            linear_label.move_to(LEFT * 3.5 + UP * 2.2)
            
            lin_node1 = self.create_node("A", LEFT * 5 + UP * 0.8)
            lin_node2 = self.create_node("B", LEFT * 3.5 + UP * 0.8)
            lin_node3 = self.create_node("C", LEFT * 2 + UP * 0.8)
            lin_null = self.create_node("×", LEFT * 0.5 + UP * 0.8, is_null=True)
            
            lin_arrow1 = Arrow(lin_node1.get_right(), lin_node2.get_left(), 
                              buff=0.05, stroke_width=3, color=YELLOW)
            lin_arrow2 = Arrow(lin_node2.get_right(), lin_node3.get_left(), 
                              buff=0.05, stroke_width=3, color=YELLOW)
            lin_arrow3 = Arrow(lin_node3.get_right(), lin_null.get_left(), 
                              buff=0.05, stroke_width=3, color=RED)
            
            linear_group = VGroup(lin_node1, lin_node2, lin_node3, lin_null, 
                                 lin_arrow1, lin_arrow2, lin_arrow3)
            
            # Circular list on right
            circular_label = Text("Circular", font_size=24, color=GREEN)
            circular_label.move_to(RIGHT * 3.5 + UP * 2.2)
            
            circ_node1 = self.create_node("A", RIGHT * 2 + UP * 0.8)
            circ_node2 = self.create_node("B", RIGHT * 3.5 + UP * 0.8)
            circ_node3 = self.create_node("C", RIGHT * 5 + UP * 0.8)
            
            circ_arrow1 = Arrow(circ_node1.get_right(), circ_node2.get_left(), 
                               buff=0.05, stroke_width=3, color=YELLOW)
            circ_arrow2 = Arrow(circ_node2.get_right(), circ_node3.get_left(), 
                               buff=0.05, stroke_width=3, color=YELLOW)
            circ_arrow3 = CurvedArrow(circ_node3.get_top() + UP * 0.05, 
                                     circ_node1.get_top() + UP * 0.05,
                                     color=GREEN, angle=-TAU/4)
            
            circular_group = VGroup(circ_node1, circ_node2, circ_node3, 
                                   circ_arrow1, circ_arrow2, circ_arrow3)
            
            self.play(Write(linear_label), Write(circular_label))
            self.play(Create(linear_group), Create(circular_group))
            
        with self.voiceover(text="In terms of use cases, linear linked lists are better when you have a clear start and end, such as implementing a stack or a simple queue. Circular linked lists excel when you need continuous cycling, like in round-robin scheduling or playlist management. The choice depends entirely on whether your application naturally has endpoints or operates in cycles.") as tracker:
            comparison = VGroup(
                Text("Linear: Clear endpoints, easier traversal", font_size=18),
                Text("Circular: Continuous loops, cyclic operations", font_size=18)
            ).arrange(DOWN, buff=0.4)
            comparison.move_to(DOWN * 2.2)
            
            for comp in comparison:
                self.play(Write(comp), run_time=0.8)
                
        # Cleanup
        self.play(FadeOut(*self.mobjects))

    def conclusion(self):
        """Wrap up the explanation"""
        with self.voiceover(text="We've covered a comprehensive exploration of circular linked lists, from their basic structure to advanced operations and real-world applications. Let's summarize the key takeaways from today's lesson.") as tracker:
            title = Text("Summary", font_size=36, color=BLUE, weight=BOLD)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
        with self.voiceover(text="Circular linked lists are a powerful variation of the standard linked list where the last node points back to the first, creating a continuous loop. This structure enables efficient cyclic operations and eliminates the need for null pointer checks. They're particularly useful in operating system scheduling, game turn management, and media player playlists.") as tracker:
            key_points = VGroup(
                Text("✓ Last node points to first node", font_size=22),
                Text("✓ No null pointers - continuous loop", font_size=22),
                Text("✓ Perfect for cyclic operations", font_size=22),
                Text("✓ Used in OS scheduling & media players", font_size=22),
                Text("✓ Requires careful traversal logic", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
            key_points.move_to(DOWN * 0.5)
            
            for point in key_points:
                self.play(Write(point), run_time=0.7)
                self.wait(0.3)
                
        with self.voiceover(text="Remember that while circular linked lists offer unique advantages, they also require more careful implementation to avoid infinite loops. Always track your starting position during traversal, and consider maintaining a tail pointer for optimal performance. With practice, you'll develop an intuition for when circular linked lists are the right choice for your data structure needs. Thank you for watching, and happy coding!") as tracker:
            self.wait(2)
            
            # Final thank you
            self.play(FadeOut(*self.mobjects))
            
            thank_you = Text("Thank You!", font_size=36, color=BLUE, weight=BOLD)
            learn_more = Text("Keep exploring data structures!", font_size=24, color=WHITE)
            final_group = VGroup(thank_you, learn_more).arrange(DOWN, buff=0.5)
            
            self.play(Write(thank_you))
            self.play(FadeIn(learn_more))
            self.wait(2)

    def create_node(self, data, position, is_null=False):
        """Helper function to create a node visualization"""
        if is_null:
            circle = Circle(radius=0.4, color=RED, fill_opacity=0.2, stroke_width=2)
            text = Text(data, font_size=24, color=RED)
        else:
            circle = Circle(radius=0.4, color=WHITE, fill_opacity=0.1, stroke_width=2)
            text = Text(str(data), font_size=24)
        
        text.move_to(position)
        circle.move_to(position)
        
        return VGroup(circle, text)

# To render the animation, run:
# manim -pql circular_linked_list.py CircularLinkedListExplanation