#include <bits/stdc++.h> 
using namespace std;
void Neosxristis();
bool egkyroemail(string);
bool egkyroonoma(string);
bool egkyroepitheto(string);
bool egkyroskodikos(string);
void kodikosepalitheusis();
void Syndetheite();
int main()
{
    
    cout << "Ayth einai h selida mas" << endl;
    Neosxristis();

    return 0;
}
void Neosxristis() {
	string Neaeggrafi,onomaxristi,kodikos,onoma,epitheto,email;
	cout << "Eiste kainourgios xristis;";  
    
    cin >> Neaeggrafi; // must be "yes" if he is a new user or "no" if he is not a new user
    cin.ignore();
    if (Neaeggrafi == "Yes" || Neaeggrafi == "yes" )
    {
        cout << "Onoma: "; // eisagogi onomatos
        cin >> onoma;
        while (egkyroonoma(onoma) == false)
        {
            cout << "Den einai egkyro to onoma sas, prospathiste ek neou: " << endl;
            cin >> onoma;
        }
        cout << endl
             << "Egkyro to onoma." << endl
             << endl;


        cout << "Epitheto: "; // eisagogi epithetou
        cin >>epitheto ;
        while (egkyroepitheto(epitheto) == false)
        {
            cout << "Den einai egkyro to epitheto sas, prospathiste pali: " << endl;
            cin >> epitheto;
        }
        cout << endl
             << "Egkyro to epitheto." << endl
             << endl;

        cout << "Email : "; // enter email
        cin >> email;
        while (egkyroemail(email) == false)
        {
            cout << "Mh egkyro email, prospathiste pali: " << endl;
            cin >> email;
        }
        cout << endl
             << "Email egkyro." << endl
             << endl;

        cout << "Kodikos : \n(O kodikos prepei na periexei toulaxiston ena psifio, ena mikro gramma, ena kefalaio gramma kai enan eidiko xaraktira px teleia.) \n"; // eisagogi kodikou
        cin >> kodikos;
        while (egkyroskodikos(kodikos) == false)
        {
            cout << "Mh egkyros kodikos, prospathiste pali: " << endl;
            cin >> kodikos;
        }
        cout << endl
             << "Egkyros kodikos." << endl
             << endl;

        cout << "Epityxhs eggrafh" << endl;
        kodikosepalitheusis();
    }
    else if (Neaeggrafi == "No"  ||Neaeggrafi == "no") 
    {
		string onomaxristi, kodikos;
    cout << endl<< "-----Syndetheite-----" << endl<< endl;
    cout << "Onoma xristi:" << endl;
    getline(cin, onomaxristi);

    cout << "Kodikos:" << endl;
    cin >> kodikos;

    cout << endl
         << "Epityxhs syndesh" << endl;
    }
}
bool egkyroonoma(string onoma) //elegxos orthis eisagogis onomatos
{
    if (onoma[0] >= 'A' && onoma[0] <= 'Z')
      return true;
	  else
	  return false;
}
bool egkyroepitheto(string epitheto) //elegxos orthis eisagogis epithetou
{
    if (epitheto[0] >= 'A' && epitheto[0] <= 'Z')
      return true;
    
    else 
  	 return false;
       
    
}
bool egkyroemail(string email) //elegxos egkyrothtas email
{
    int papaki = -1, teleia = -1;                                                            // variables to store the position of ( @ )and (dot)
    int papakicounter = 0, teleiacounter = 0;                                          // check if there is more than one (@) or (dot)
    if ((email[0] >= 'a' && email[0] <= 'z') || (email[0] >= 'A' && email[0] <= 'Z')) //to email prepei na arxizei me gramma
    {
        for (int i = 0; i < email.length(); i++)
        {
            if (email[i] == '@') //O xaraktiras einai '@'
            {
                papaki = i;
                ++papakicounter;
            }

            else if (email[i] == '.') //O xaraktiras einai dot
            {
                teleia = i;
                ++teleiacounter;
            }
        }
        if (papaki == -1 || teleia == -1) //Den yparxei @ h dot

            return false;

        if (papaki > teleia) // If (dot) is present before(@)

            return false;

        if (teleiacounter > 1 || papakicounter > 1)
            return false;

        return !(teleia >= (email.length() - 1));
    }
    else if (email[0] >= '0' && email[0] <= '9') // to email den mporei na ksekinaei me arithmo
    {
        return false;
    }
    else //oyte me symvola mporei na ksekinaei ena email
    {
        return false;
    }
}
bool egkyroskodikos(string kodikos) // elegxos orthis eisagogis kodikou
{
    int psifio = 0, kefalaiogramma = 0, mikrogramma = 0, eidikosxar = 0; //prepei na periexei toulaxiston ena psifio, ena kefalaio gramma, ena mikro gramma kai enan eidiko xaraktira
    if (kodikos.length() >= 8 && kodikos.length() <= 15)
    {

        if (kodikos.find(" ") == -1)
        {
            for (int i = 0; i < kodikos.length(); i++)
            {
                if (kodikos[i] >= '0' && kodikos[i] <= '9')
                {
                    ++psifio;
                }
                else if (kodikos[i] >= 'a' && kodikos[i] <= 'z')
                {
                    ++mikrogramma;
                }
                else if (kodikos[i] >= 'A' && kodikos[i] <= 'Z')
                {
                    ++kefalaiogramma;
                }
                else if (kodikos[i] == '@' || kodikos[i] == '#' || kodikos[i] == '_')
                {
                    ++eidikosxar;
                }
            }

            if (psifio == 0 || kefalaiogramma == 0 || mikrogramma == 0 || eidikosxar == 0)
            {
                return false;
            }
            else
            {
                return true;
            }
        }
        else if (kodikos.find(" ") != -1)
        {

            return false;
        }
    }
    cout << "Note : your password length less than 8 characters or more than 15 characters." << endl;
    return false;
}
void kodikosepalitheusis() // verifying account
{
    int vercode ;

    cout << "Steilame kodiko epalitheusis sto email sas pros elegxo tou logariasmou sas. Parakalo elegxte to email sas." << endl;
    cout<<"Email message: O kodikos einai: ";
    srand(time(0));

	for (int i = 0; i <= 3; i++)
	{
		cout << rand() % 10 ;
	}
    cout<<"\n";

    cout<<"Eisagete ton kodiko epalitheusis : \n";
	cin>>vercode;

    cout << "Epivevaiosame ton logariasmo sas." << endl;
    Syndetheite();
}
void Syndetheite()
{
    string Username, Password;

    cin.ignore();
    cout << endl    <<"-----Syndetheite-----" << endl<< endl;
    cout << "Eisagete to onoma xristi:" << endl;
    getline(cin, Username);

    cout << "Eisagete ton kodiko sas:" << endl;
    cin >> Password;

    cout << endl
         << "Epityxhs syndesh" << endl;
}
