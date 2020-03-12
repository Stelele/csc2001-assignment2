import java.nio.file.*;
import java.io.FileWriter;

/**
 * helper class containing methods useful in other classes
 * */
public class LSHelper
{
	/**
	* function that reads in all the contents of a file and returns the string output of the file
	* @param fileName <code>String</code> represents the location of the file to be read in
	* @throws Exception in case the file is not found
	* @return fileString <code>String</code> represents String output of the file
	* */
	public static String readFileAsString(String fileName) throws Exception
	{
		String data = "";
		data = new String(Files.readAllBytes(Paths.get(fileName)));

		return data;
	}

	/**
	* function that writes to a specified file
	* @param fileName <code>String</code> represents the file location to be writen to
	* @param text <code>String</code> represents the text to be outputed to the file
	* @throws Exception if writing to file failed
	* */
	public static void writeToFile(String fileName,String text) throws Exception
	{
		FileWriter newFile = new FileWriter(fileName);
		newFile.write(text);
		newFile.close();
	}

	public static void loadAVLTree(String fileName, AVLTree<LSData> tree) throws Exception
	{
		String entries[] = readFileAsString(fileName).split("\n");

		for(int i = 0; i < entries.length ; i++)
		{
			String entry[] = entries[i].split(" ",2);

			LSData record = new LSData(entry[0], entry[1]);

			tree.insert(record);
		}
	}

	public static void loadBinarySearchTree(String fileName, BinarySearchTree<LSData> tree) throws Exception
	{
		String entries[] = readFileAsString(fileName).split("\n");

		for(int i = 0; i < entries.length; i++)
		{
			String entry[] = entries[i].split(" ",2);

			LSData record = new LSData(entry[0], entry[1]);

			tree.insert(record);
		}
	}
}
