public class BSTApp
{
	public static void main(String [] args)
	{
		String fileLocation = "/home/gift/Documents/CSC2001F/Assignment2/input/Load_Shedding_All_Areas_Schedule_and_Map.clean.final.txt";
		if(args.length == 4)
			fileLocation = args[3];

		BinarySearchTree<LSData> tree = new BinarySearchTree<LSData>();

		try
		{
			LSHelper.loadBinarySearchTree(fileLocation, tree);

			if(args.length > 0)
			{
				String key = args[0] + "_" + args[1] + "_" + args[2];

				BinaryTreeNode<LSData> found = tree.find(new LSData(key,""));

				if(found != null)
					System.out.println(found.data.getRegions() + "\n" + Integer.toString(tree.getComparisons()) +" comparisons");
				else
					System.out.println("Areas not found");
			}
			else
			{
				tree.inOrder();
			}
		}
		catch(Exception e)
		{
			System.err.println("Could not load data from file");
		}


	}
}
