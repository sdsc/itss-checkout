#!/usr/local/bin/perl -w
use strict; 
use SOAP::Lite; 
my $USE_PROXY_SERVER = 1; 
my $soap = new SOAP::Lite; 
main(@ARGV);
sub main
{
	#my $col = $ARGV[0];
	#my $table = $ARGV[1];
	#my $reqCol = $ARGV[2];
	#my $reqVal = $ARGV[3];
	#my $un = $ARGV[4];
	#my $pw = $ARGV[5];
	#my $url = $ARGV[6];
	#my $proxy = $ARGV[7];
	
	my $soap = new SOAP::Lite;
	$soap->uri('URI'); 
	$soap->proxy('PROXY'); 

	my $soapenv = $soap->MRWebServices__search( 
		'username', 
		'password', 
		'', 
		'SQLSTATEMENT'
	); 

	my $result; 
	
	if( $soapenv->fault ) 
	{ 
		print ${$soapenv->fault}{faultstring} . "\n"; 
		exit; 
	} 
	else
	{ 
		$result = $soapenv->result; 
	} 
	
	my @result_list = @{$result}; 
	for( my $i = 0; $i <= $#result_list; $i++ )
	{ 
		print "RESULT $i\n"; 
		my $hash_ref = $result_list[$i]; 
		
		foreach my $item ( keys %{$hash_ref} )
		{ 
			my $val = $hash_ref->{$item}; 
			print "$item = '$val'\n"; 
		} 
		
		print "---------------------\n"; 
	}
} 
